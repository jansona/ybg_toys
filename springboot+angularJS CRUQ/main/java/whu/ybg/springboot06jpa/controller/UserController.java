package whu.ybg.springboot06jpa.controller;

import com.fasterxml.jackson.databind.util.JSONPObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Example;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import whu.ybg.springboot06jpa.User;
import whu.ybg.springboot06jpa.repository.UserRepository;

import javax.swing.text.html.parser.Parser;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;

@Controller
public class UserController {

    @Autowired
    UserRepository userRepository;

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public String index(){
        System.out.println("inside mainController");
        return "index";
    }

    @ResponseBody
    @PostMapping("/user")
    public List<User> getUser(@RequestBody Object newObj){
            String keyword = (String)((HashMap)newObj).get("keyword");
            String method = (String)((HashMap)newObj).get("method");
            if(keyword=="" || keyword==null){return userRepository.findAll();}
            User exampleUser = new User();
            switch(method)
            {
                case "id":
                    exampleUser.setId(Integer.parseInt(keyword));
                    System.out.println(exampleUser.getId());
                    break;
                case "name":
                    exampleUser.setName(keyword);
                    break;
                case "email":
                    exampleUser.setEmail(keyword);
                    break;
            }
            Example<User> example = Example.of(exampleUser);
            List<User> users = userRepository.findAll(example);
        return users;
    }

    @ResponseBody
    @PostMapping("/user/add")
    public int insertUser(@RequestBody Object newObj){
        String name = (String)((HashMap)newObj).get("name");
        String email = (String)((HashMap)newObj).get("email");
        User newUser = new User();
        newUser.setName(name);
        newUser.setEmail(email);
        userRepository.save(newUser);

        return 0;
    }

    @GetMapping("/query")
    public String query(){
        return "query";
    }

    @ResponseBody
    @PostMapping("/user/remove/")
    public List<User> removeUser(@RequestBody Object newObj){
        Integer id = (Integer)((HashMap)newObj).get("ID");
        userRepository.deleteById(id);
        String keyword = (String)((HashMap)newObj).get("keyword");
        String method = (String)((HashMap)newObj).get("method");
        if(keyword=="" || keyword==null){return userRepository.findAll();}
        User exampleUser = new User();
        switch(method)
        {
            case "id":
                exampleUser.setId(Integer.parseInt(keyword));
                System.out.println(exampleUser.getId());
                break;
            case "name":
                exampleUser.setName(keyword);
                break;
            case "email":
                exampleUser.setEmail(keyword);
                break;
        }
        Example<User> example = Example.of(exampleUser);
        List<User> users = userRepository.findAll(example);
        return users;
    }

    @ResponseBody
    @PostMapping("/user/update")
    public User updateUser(@RequestBody Object newObj){
        Integer id = (Integer)((HashMap)newObj).get("id");
        User user = userRepository.findById(id).get();
        String name = (String)((HashMap)newObj).get("name");
        String email = (String)((HashMap)newObj).get("email");
        user.setName(name);
        user.setEmail(email);
        userRepository.flush();
        return user;
    }

    @ResponseBody
    @GetMapping("/user")
    public List<User> showUsers(){
        List<User> userList = userRepository.findAll();
        return userList;
    }
}
