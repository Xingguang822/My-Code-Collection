package org.example.service.impl;


import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.example.mapper.EmpLogMapper;
import org.example.pojo.EmpLog;
import org.example.pojo.PageResult;
import org.example.service.EmpLogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class EmpLogServiceImpl implements EmpLogService {

    @Autowired
    private EmpLogMapper empLogMapper;

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    @Override
    public void insertLog(EmpLog empLog) {
        empLogMapper.insert(empLog);
    }

    @Override
    public PageResult<EmpLog> page(Integer page, Integer pageSize) {
        PageHelper.startPage(page, pageSize);
        List<EmpLog> list = empLogMapper.list();
        Page<EmpLog> p = (Page<EmpLog>) list;
        return new PageResult<>(p.getTotal(), p.getResult());
    }
}