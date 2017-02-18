package com.sandbox.controllers;

import com.sandbox.models.User;
import com.sandbox.services.DatabaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.sql.Types;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
public class SqlController {

    @Autowired
    private DatabaseService databaseService;

    @RequestMapping("/create")
    public void create(){
        databaseService.addUser();
    }

    @RequestMapping("/select/all")
    public List<User> selectAll() {
        return databaseService.selectAll();
    }

    @RequestMapping("/select/selected")
    public List<User> selectSelected() { return databaseService.selectSelected(); }

    @RequestMapping("/select/pass")
    public List<User> selectPass() { return databaseService.selectPass(); }

    @RequestMapping("/select/salary")
    public List<User> selectSalary() {
        return databaseService.selectSalary();
    }

    @RequestMapping("/select/fail-salary")
    public List<User> selectFailAndSalary() { return databaseService.selectFailAndSalary(); }

    @RequestMapping("/update/pass")
    public void updatePass() { databaseService.updatePass(); }

    @RequestMapping("/delete/fail")
    public void deleteFail() { databaseService.deleteFailing(); }

    @RequestMapping("/select/like")
    public List<User> selectLike() {
        return databaseService.selectLike();
    }

    @RequestMapping("/select/top")
    public List<User> selectTop() {
        return databaseService.selectTop();
    }

    @RequestMapping("/select/order")
    public List<User> selectOrder() {
        return databaseService.selectOrder();
    }

    @RequestMapping("/select/group")
    public List<User> selectGroup() {
        return databaseService.selectGroup();
    }

    @RequestMapping("/select/distinct")
    public List<User> selectDistinct() {
        return databaseService.selectDistinct();
    }

    @RequestMapping("/select/sort")
    public List<User> selectSort() {
        return databaseService.selectSort();
    }
}