package org.example.controller;

import lombok.extern.slf4j.Slf4j;
import org.example.pojo.Emp;
import org.example.pojo.EmpQueryParam;
import org.example.pojo.PageResult;
import org.example.pojo.Result;
import org.example.service.EmpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/emps")
@Slf4j
@RestController
public class EmpController {

    @Autowired
    private EmpService empService;

    /*@GetMapping
    public Result page(@RequestParam(defaultValue ="1") Integer page,
                       @RequestParam(defaultValue ="10") Integer pageSize,
                       String name, Integer gender,
                       @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate begin,
                       @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate end){
        log.info("分页查询：{}，{},{},{},{},{}",page,pageSize,name,gender,begin,end);
        PageResult<Emp> pageResult=empService.page(page,pageSize,name,gender,begin,end);
        return Result.success(pageResult);
    }*/

    @GetMapping
    public Result page(EmpQueryParam empQueryParam){
        log.info("分页查询：{}",empQueryParam);
        PageResult<Emp> pageResult=empService.page(empQueryParam);
        return Result.success(pageResult);
    }

    @PostMapping
    public Result save(@RequestBody Emp emp){
        log.info("新增员工：{}",emp);
        empService.save(emp);
        return Result.success();
    }

    /*@DeleteMapping
    public Result delete(Integer[] ids){
        log.info("删除员工{}", Arrays.toString(ids));
        return Result.success();

    }*/

    @DeleteMapping
    public Result delete(@RequestParam List<Integer> ids){
        log.info("删除员工{}", ids);
        empService.delete(ids);
        return Result.success();
    }

    @GetMapping("/{id}")
    public Result getInfo(@PathVariable Integer id){
        log.info("根据id查询员工信息{}", id);
        Emp emp= empService.getInfo(id);
        return Result.success(emp);
    }

    @PutMapping
    public Result update(@RequestBody Emp emp){
        log.info("修改员工{}", emp);
        empService.update(emp);
        return Result.success();
    }
}
