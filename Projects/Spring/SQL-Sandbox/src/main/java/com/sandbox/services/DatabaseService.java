package com.sandbox.services;

import com.sandbox.models.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import java.sql.Types;
import java.util.List;

@Configuration
public class DatabaseService {

    @Autowired
    JdbcTemplate jdbcTemplate;

    public void addUser(){
        final String QUERY = "insert into users(name,email) values(?,?)";

        Object[] params = {"Ryan", "Newman"};
        int[] types = {Types.VARCHAR, Types.VARCHAR};

        jdbcTemplate.update(QUERY, params, types);
    }

    public List<User> selectAll(){
        final String QUERY = "select * from users";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            return user;
        });
    }

}
