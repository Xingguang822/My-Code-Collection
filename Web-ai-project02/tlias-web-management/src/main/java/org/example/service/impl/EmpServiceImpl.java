package org.example.service.impl;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.example.mapper.EmpMapper;
import org.example.pojo.Emp;
import org.example.pojo.PageResult;
import org.example.service.EmpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmpServiceImpl implements EmpService {

    @Autowired
    private EmpMapper empMapper;

    /*@Override
    public PageResult<Emp> page(Integer page, Integer pageSize) {
        long total=empMapper.count();
        List<Emp> rows=empMapper.list((page-1)*pageSize,pageSize);
        return new PageResult<Emp>(total,rows);
    }*/

    /*PageHelper注意事项：
    *                   1.SQL语句结尾不能加分号
    *                   2.PageHelper仅能对紧跟在其后的第一个查询语句进行分页处理
    * */
    public PageResult<Emp> page(Integer page, Integer pageSize) {
        PageHelper.startPage(page,pageSize);
        List<Emp> empList = empMapper.list();
        Page<Emp> p=(Page<Emp>) empList;
        return new PageResult<Emp>(p.getTotal(),p.getResult());
    }
}
