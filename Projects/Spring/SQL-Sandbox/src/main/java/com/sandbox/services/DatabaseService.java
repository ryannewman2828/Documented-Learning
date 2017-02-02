package com.sandbox.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import java.sql.Types;

@Configuration
public class DatabaseService {

    @Autowired
    JdbcTemplate jdbcTemplate;

    public void addUser(){
        final String query = "insert into users(name,email) values(?,?)";

        Object[] params = {"Ryan", "Newman"};
        int[] types = {Types.VARCHAR, Types.VARCHAR};

        jdbcTemplate.update(query, params, types);
    }

}
