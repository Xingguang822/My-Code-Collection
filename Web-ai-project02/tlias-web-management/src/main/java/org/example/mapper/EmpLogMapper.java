package org.example.mapper;


import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.example.pojo.EmpLog;

import java.util.List;

@Mapper
public interface EmpLogMapper {

    @Insert("insert into emp_log (operate_emp_id, operate_time, class_name, method_name, method_params, return_value, cost_time) " +
            "values (#{operateEmpId}, #{operateTime}, #{className}, #{methodName}, #{methodParams}, #{returnValue}, #{costTime})")
    public void insert(EmpLog empLog);

    @Select("select l.*, e.name operateEmpName from emp_log l left join emp e on l.id = e.id order by l.operate_time desc")
    List<EmpLog> list();
}