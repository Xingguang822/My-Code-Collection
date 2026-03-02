package org.example.service.impl;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.example.mapper.EmpExprMapper;
import org.example.mapper.EmpMapper;
import org.example.pojo.*;
import org.example.service.EmpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.CollectionUtils;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class EmpServiceImpl implements EmpService {

    @Autowired
    private EmpMapper empMapper;

    @Autowired
    private EmpExprMapper empExprMapper;

    @Autowired
    private EmpLogServiceImpl empLogService;

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
    public PageResult<Emp> page(EmpQueryParam empQueryParam) {
        PageHelper.startPage(empQueryParam.getPage(),empQueryParam.getPageSize());
        List<Emp> empList = empMapper.list(empQueryParam);
        Page<Emp> p=(Page<Emp>) empList;
        return new PageResult<Emp>(p.getTotal(),p.getResult());
    }

    @Transactional(rollbackFor = {Exception.class})//默认出现运行时异常才回滚
    @Override
    public void save(Emp emp) {
        try {
            emp.setCreateTime(LocalDateTime.now());
            emp.setUpdateTime(LocalDateTime.now());
            empMapper.insert(emp);

            List<EmpExpr> exprList=emp.getExprList();
            if(!CollectionUtils.isEmpty(exprList)){
                exprList.forEach(empExpr ->
                        empExpr.setEmpId(emp.getId())
                );
                empExprMapper.insertBatch(exprList);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            EmpLog empLog=new EmpLog(null,LocalDateTime.now(),"新增员工："+emp);
            empLogService.insertLog(empLog);
        }

    }
}
