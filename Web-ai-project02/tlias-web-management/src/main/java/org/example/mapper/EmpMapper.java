package org.example.mapper;

import org.apache.ibatis.annotations.*;
import org.example.pojo.Emp;
import org.example.pojo.EmpQueryParam;
import org.example.pojo.JobOption;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

@Mapper
public interface EmpMapper {
    /*@Select("SELECT COUNT(*) FROM emp e LEFT JOIN dept d ON e.dept_id=d.id ")
    public long count();

    @Select("SELECT e.*,d.name deptName FROM emp e LEFT JOIN dept d ON e.dept_id=d.id " +
            "ORDER BY e.update_time DESC LIMIT #{start},#{pageSize}")
    public List<Emp> list(Integer start,Integer pageSize);*/

    //@Select("SELECT e.*,d.name deptName FROM emp e LEFT JOIN dept d ON e.dept_id=d.id ORDER BY e.update_time WHERE e.name LIKE %#{name}% AND e.gender=#{gender} AND e.create_time BEWTEEN #{begin} AND #{end}")
    public List<Emp> list(EmpQueryParam empQueryParam);

    @Options(useGeneratedKeys = true,keyProperty = "id")
    @Insert("INSERT INTO emp(username, name, gender, phone, job, salary, image, entry_date, dept_id, create_time, update_time)\n" +
            "       VALUES(#{username}, #{name}, #{gender}, #{phone}, #{job}, #{salary}, #{image}, #{entryDate}, #{deptId}, #{createTime}, #{updateTime})")
    void insert(Emp emp);

    void deleteByIds(List<Integer> ids);

    Emp getById(Integer id);

    void updateById(Emp emp);

    @MapKey("pos")
    List<Map<String,Object>> countEmpJobData();

    @MapKey("name")
    List<Map<String, Object>> countEmpGenderData();

    Emp selectByUsernameAndPassword(Emp emp);
}
