package org.example.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.example.pojo.Emp;

import java.util.List;

@Mapper
public interface EmpMapper {

    /*@Select("SELECT COUNT(*) FROM emp e LEFT JOIN dept d ON e.dept_id=d.id ")
    public long count();

    @Select("SELECT e.*,d.name deptName FROM emp e LEFT JOIN dept d ON e.dept_id=d.id " +
            "ORDER BY e.update_time DESC LIMIT #{start},#{pageSize}")
    public List<Emp> list(Integer start,Integer pageSize);*/

    @Select("SELECT e.*,d.name deptName FROM emp e LEFT JOIN dept d ON e.dept_id=d.id ORDER BY e.update_time ")
    public List<Emp> list();
}
