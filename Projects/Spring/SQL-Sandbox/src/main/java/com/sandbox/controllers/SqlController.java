package com.sandbox.controllers;

import com.sandbox.services.DatabaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.Types;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@RestController
public class SqlController {

    @Autowired
    private DatabaseService databaseService;

    @RequestMapping("/greet")
    public Map<String,Object> home() {
        Map<String,Object> model = new HashMap<String,Object>();
        model.put("id", UUID.randomUUID().toString());
        model.put("content", "Hello World");
        return model;
    }

    @RequestMapping("/create")
    public void create(){
        databaseService.addUser();
    }

}