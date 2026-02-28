package org.example.controller;

import jakarta.servlet.http.HttpServletRequest;
import lombok.extern.flogger.Flogger;
import org.apache.ibatis.annotations.Insert;
import org.example.pojo.Dept;
import org.example.pojo.Result;
import org.example.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/depts")
@RestController
public class DeptController {

    @Autowired
    private DeptService deptService;

    /*@RequestMapping(value = "/depts",method = RequestMethod.GET)*/
    @GetMapping
    public Result list() {
        System.out.println("查询全部部门数据");
        List<Dept> deptList = deptService.findall();
        return Result.success(deptList);
    }

    /*方式一：繁琐
    @DeleteMapping("/depts")
    public Result delete(HttpServletRequest request){
        String idStr=request.getParameter("id");
        int id=Integer.parseInt(idStr);
        System.out.println("根据ID删除部门："+id);
        return Result.success();
    }*/

    /*方式二：@RequestParam参数必须传递，不传递将会报错
    @DeleteMapping("/depts")
    public Result delete(@RequestParam("id") Integer deptid){
        System.out.println("根据ID删除部门："+deptid);
        return Result.success();
    }*/
    /*方式三：省略@RequestParam（前短传递的请求参数名与服务端方法形参名一致）*/
    @DeleteMapping
    public Result delete(Integer id) {
        System.out.println("根据ID删除部门：" + id);
        deptService.deleteByID(id);
        return Result.success();
    }

    @PostMapping
    public Result add(@RequestBody Dept dept){
        System.out.println("新增部门"+dept);
        deptService.add(dept);
        return Result.success();
    }

    @GetMapping("/{id}")
    public Result getInfo(@PathVariable Integer id){
        System.out.println("根据ID查询部门"+id);
        Dept dept=deptService.getById(id);
        return Result.success(dept);
    }

    @PutMapping
    public Result update(@RequestBody Dept dept){
        System.out.println("修改部门"+dept);
        deptService.update(dept);
        return Result.success();
    }

}
