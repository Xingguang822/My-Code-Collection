package org.example.mapper;

import org.apache.ibatis.annotations.*;
import org.example.pojo.Dept;

import java.util.List;

@Mapper
public interface DeptMapper {
    /*查询所有部门信息*/
    /*//1
    @Results({
            @Result(column="create_time",property = "createTime"),
            @Result(column="update_time",property = "updateTime")
    })*/
    /*//    2.起别名
    @Select("SELECT id,name,create_time createTime,update_time updateTime from dept order by update_time desc")*/
    @Select("SELECT id,name,create_time,update_time from dept order by update_time desc")
    List<Dept> findall();

    @Delete("DELETE FROM dept WHERE id=#{id}")
    void deleteById(Integer id);

    @Insert("INSERT INTO dept(name,create_time,update_time) VALUES(#{name},#{createTime},#{updateTime}) ")
    void insert(Dept dept);

    @Select("SELECT id,name,create_time,update_time FROM dept WHERE id=#{id}")
    Dept getById(Integer id);

    @Update("UPDATE dept SET name=#{name},update_time=#{updateTime} WHERE id=#{id}")
    void update(Dept dept);
}
