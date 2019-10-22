from functools import reduce
import copy


class Item(object):

    def __init__(self, item_set=None, sup=0, node_link=None):
        self.item_set = item_set
        self.sup = sup
        self.node_link = node_link


class FPTableItem(object):

    def __init__(self, post_items):
        self.post_items = post_items
        self.cond_pattern_base = []


class TreeNode(object):

    def __init__(self, item, count=0, parent=None, node_link=None):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = []
        self.node_link = node_link

    def __eq__(self, other):
        # if type(other) is not Item:
        #     print(False)
        #     return False
        
        # print(self.item == other)
        # print(self.item, other)
        return self.item == other

    def __getitem__(self, item):

        for child in self.children:
            if child.item == item:
                return child
        
        raise KeyError


class FP_Growth(object):

    def __init__(self, TDB, sup_threshold=2):
        self.TDB = TDB
        self.sup_threshold = sup_threshold

        self.fp_patterns = []

    def sup_count(self, item):
        return sum([(not item.difference(items)) for items in self.TDB.values()])

    def __call__(self):

        # Get L
        all_item = reduce(lambda x, y: x.union(y), self.TDB.values())
        C = [{item} for item in all_item]
        L = {list(item_set)[0]:(Item(list(item_set)[0], self.sup_count(item_set), None)) for item_set in C}
        self.L = L

        for item in L:
            self.fp_patterns.append(([item], L[item].sup))

        for key in self.TDB.keys():
            self.TDB[key] = [(item, L[item].sup) for item in self.TDB[key]]
            self.TDB[key] = [item for item in filter(lambda x:x[1]>=self.sup_threshold, self.TDB[key])]
            self.TDB[key] = sorted(self.TDB[key], key=lambda elem:elem[1], reverse=True)
            # print(self.TDB[key])

        # build tree
        root_node = TreeNode(item=None, count=None, parent=None, node_link=None)

        def add_node_link(item, tree_node):
            end_node = L[item]

            while end_node.node_link is not None:
                end_node = end_node.node_link

            end_node.node_link = tree_node

        for items in self.TDB.values():
            items = [item[0] for item in items]

            curr_node = root_node
            for item in items:

                if item in curr_node.children:
                    curr_node = curr_node[item]
                    curr_node.count += 1
                else:
                    new_node = TreeNode(item=item, count=1, parent=curr_node)
                    curr_node.children.append(new_node)
                    add_node_link(item, new_node)
                    
                    curr_node = curr_node[item]

        # get conditional pattern base
        self.fp_table = dict()
        for item in self.L.keys():
            self.fp_table[item] = FPTableItem([item])

            node = self.L[item].node_link

            while node is not None:

                parent = node.parent
                
                parents = []
                while parent is not None and parent.item is not None:
                    parents.append(parent.item)
                    parent = parent.parent

                parents.reverse()
                self.fp_table[item].cond_pattern_base.append((parents, node.count))

                node = node.node_link

        def generate_tree(cond_pattern_base, post_items):

            def filter_base_and_add_fp():
                nonlocal post_items

                temp_d = dict()

                for base in cond_pattern_base:
                    count = base[1]
                    items = base[0]

                    for item in items:
                        temp_d[item] = temp_d.get(item, 0) + count
                
                for j in range(len(cond_pattern_base)):
                    base = cond_pattern_base[j]
                    new_list = copy.deepcopy(base[0])
                    for i in range(len(base[0])):
                        if temp_d[base[0][i]] < self.sup_threshold:
                            del new_list[i]
                        # else:
                            # self.fp_patterns.append(([base[0][i]]+post_items, temp_d[base[0][i]]))
                    cond_pattern_base[j] = (new_list, base[1])

                for item in temp_d:
                    if temp_d[item] >= self.sup_threshold:
                        self.fp_patterns.append(([item]+post_items, temp_d[item]))

            filter_base_and_add_fp()

            root_node = TreeNode(item=None, count=None, parent=None, node_link=None)
            L = dict()

            for base in cond_pattern_base:
                count = base[1]
                items = base[0]

                curr_node = root_node
                for item in items:

                    if item in curr_node.children:
                        curr_node = curr_node[item]
                        curr_node.count += count
                    else:
                        new_node = TreeNode(item=item, count=count, parent=curr_node)
                        curr_node.children.append(new_node)

                        # 将新节点插入到node link尾部
                        if item not in L.keys():
                            L[item] = Item(item_set=item, node_link=None)

                        end_node = L[item]
                        while end_node.node_link is not None:
                            end_node = end_node.node_link

                        end_node.node_link = new_node
                        
                        curr_node = curr_node[item]

            if len(L) == 0:
                return
            
            # 对每一个item寻找条件模式基，并造树
            for item in L.keys():

                new_cond_base = []
                node = L[item].node_link

                while node is not None:
                    
                    new_cond_base.append(([], node.count))
                    parent = node.parent

                    while parent is not None and parent.item is not None:
                        new_cond_base[-1][0].append(parent.item)
                        parent = parent.parent
                    
                    new_cond_base[-1][0].reverse()

                    node = node.node_link

                generate_tree(new_cond_base, [item]+post_items)
        
        for item in self.fp_table:
            fp_item = self.fp_table[item]
            generate_tree(fp_item.cond_pattern_base, fp_item.post_items)

        return self.fp_patterns

    def show_same_nodes(self, item):
        node = self.L[item].node_link

        while node is not None:
            print("{}:{}".format(node.item, node.count))
            node = node.node_link

    def show_fp_table(self):

        for item in self.fp_table.keys():
            print(item)
            print(self.fp_table[item].cond_pattern_base)
            print()

    def get_support(self, item_set):

        for item in self.fp_patterns:
            if set(item[0]) == item_set:
                return item[1]
        
        return None

    def confidence(self, preset, postset):
        combined_set = preset.union(postset)

        return self.get_support(combined_set) / self.get_support(preset)

    def get_ass_rule(self, conf_threshold=0.6):

        strong_ass = []

        def get_subsets(item_set):
            sub_list_all = []
            for i in range(1 << len(item_set)):
                combo_list = list()
                for j in range(len(item_set)):
                    if i & (1 << j):
                        combo_list.append(item_set[j])
                sub_list_all.append(combo_list)

            sub_list_all.remove([])
            sub_list_all.remove(item_set)
            sub_list_all = [set(item_set_list) for item_set_list in sub_list_all]
            return sub_list_all

        for item in self.fp_patterns:
            item_set = item[0]

            sub_sets = get_subsets(item_set)

            for subset in sub_sets:
                conf = self.confidence(subset, set(item_set) - subset)

                if conf > conf_threshold:
                    strong_ass.append("{} => {} : {}".format(subset, set(item_set) - subset, conf))

        return strong_ass


def main():

    # data = {'10':{'A','C','D'}, '20':{'B','C','E'}, '30':{'A','B','C','E'}, '40':{'B', 'E'}}
    data = {'T100': {'I5', 'I1', 'I2'}, 'T200': {'I4', 'I2'}, 'T300': {'I3', 'I2'}, 
    'T400': {'I4', 'I1', 'I2'}, 'T500': {'I3', 'I1'}, 'T600': {'I3', 'I2'}, 
    'T700': {'I3', 'I1'}, 'T800': {'I5', 'I3', 'I1', 'I2'}, 'T900': {'I3', 'I1', 'I2'}}

    test_fp_growth = FP_Growth(TDB=data)

    print(test_fp_growth())

    strong_ass = test_fp_growth.get_ass_rule(0.7)

    for rule in strong_ass:
        print(rule)

    # test_fp_growth.show_same_nodes('I3')

    # test_fp_growth.show_fp_table()


if __name__ == '__main__':

    main()
