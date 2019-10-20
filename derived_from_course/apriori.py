from functools import reduce


class Item(object):

    def __init__(self, item_set=set(), sup=0):
        self.item_set = item_set
        self.sup = sup


class Apriori(object):

    def __init__(self, TDB=dict(), sup_threshold=2):
        self.TDB = TDB
        self.sup_threshold = sup_threshold
        self.total_items = []

    def sup_count(self, item):
        # all_item = reduce(lambda x, y: x.union(y), TDB.values())
        return sum([(not item.difference(items)) for items in self.TDB.values()])

    def __call__(self):

        all_item = reduce(lambda x, y: x.union(y), self.TDB.values())
        C = [{item} for item in all_item]
        L = [Item(item_set=item_set, sup=self.sup_count(item_set)) for item_set in C]

        L = [elem for elem in filter(lambda item: item.sup >= self.sup_threshold, L)]

        def generate_item():
            L_item_sets = [item.item_set for item in L]

            def issubset_in_L_item_sets(new_set):
                for item in new_set:
                    sub_set = new_set - {item}
                    
                    if sub_set not in L_item_sets:
                        return False
                    
                return True

            new_C = []

            for i in range(len(L_item_sets)):
                for j in range(i+1, len(L_item_sets)):
                    temp_set = L_item_sets[i].union(L_item_sets[j])
                    if temp_set not in new_C:
                        new_C.append(temp_set)

            new_C = [elem for elem in filter(issubset_in_L_item_sets, new_C)]
            return new_C

        while L:
            self.total_items += L 
            C = generate_item()
            L = [Item(item_set=item_set, sup=self.sup_count(item_set)) for item_set in C]
            L = [elem for elem in filter(lambda item: item.sup >= self.sup_threshold, L)]

        return len(self.total_items)

    def get_support(self, item_set):

        for item in self.total_items:
            if item.item_set == item_set:
                return item.sup
        
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

        for item in self.total_items:
            item_set = item.item_set

            sub_sets = get_subsets(list(item_set))

            for subset in sub_sets:
                conf = self.confidence(subset, item_set - subset)

                if conf > conf_threshold:
                    strong_ass.append("{} => {} : {}".format(subset, item_set - subset, conf))

        return strong_ass


def main():
    data = {'10':{'A','C','D'}, '20':{'B','C','E'}, '30':{'A','B','C','E'}, '40':{'B', 'E'}}

    test_apriori = Apriori(TDB=data)

    print(test_apriori())

    for item in test_apriori.total_items:
        print("Itemset: {}, sup: {}".format(item.item_set, item.sup))

    strong_ass = test_apriori.get_ass_rule(0.7)

    for rule in strong_ass:
        print(rule)


if __name__ == "__main__":
    main()
