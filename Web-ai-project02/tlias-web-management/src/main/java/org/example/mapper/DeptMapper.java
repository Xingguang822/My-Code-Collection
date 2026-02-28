package org.example.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.example.pojo.Dept;

import java.util.List;

@Mapper
public interface DeptMapper {
    /*查询所有部门信息*/
    @Select("SELECT id,name,create_time,update_time from dept order by update_time desc")
    List<Dept> findall();
}
