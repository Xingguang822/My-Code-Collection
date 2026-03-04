package org.example.service;

import org.example.pojo.Dept;

import java.util.List;

public interface DeptService {

    List<Dept> findall();

    void deleteByID(Integer id);

    void add(Dept dept);

    Dept getById(Integer id);

    void update(Dept dept);
}
