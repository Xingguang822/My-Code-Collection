package com.itheima;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class UserServiceTest {

    @Test
    public void testGetAge(){
        UserService userService = new UserService();
        Integer age=userService.getAge("100000200511142030");
        System.out.println(age);
    }

    @Test
    public void testGetGender(){
        UserService userService = new UserService();
        String gender=userService.getGender("100000200511142030");
        System.out.println(gender);
    }

    @Test
    public void testGenderWithAssert(){
        UserService userService = new UserService();
        String gender=userService.getGender("100000200511142030");
//        Assertions.assertEquals("男",gender);
        Assertions.assertEquals("男",gender,"性别获取逻辑有问题");
    }

    @Test
    public void testGenderWithAssert2(){
        UserService userService = new UserService();
        String gender=userService.getGender("100000200511142030");
        Assertions.assertThrows(IllegalArgumentException.class,()->{
            userService.getGender(null);
        });
    }
}
