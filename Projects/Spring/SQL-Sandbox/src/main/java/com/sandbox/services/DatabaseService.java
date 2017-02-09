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
        final String QUERY = "INSERT INTO users(name, email, salary, grade, pass) VALUES (?,?,?,?,?);";

        Object[] params = {"Ryan", "ranewman@uwaterloo.ca", 100000, 100, 1};
        int[] types = {Types.VARCHAR, Types.VARCHAR, Types.INTEGER, Types.INTEGER, Types.BIT};

        jdbcTemplate.update(QUERY, params, types);
    }

    public List<User> selectAll(){
        final String QUERY = "select * from users;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            return user;
        });
    }

    public List<User> selectSelected(){
        final String QUERY = "SELECT name, email, salary FROM users;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            return user;
        });
    }

    public List<User> selectPass(){
        final String QUERY = "SELECT * FROM users WHERE pass";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            return user;
        });
    }

    public List<User> selectSalary(){
        final String QUERY = "SELECT * FROM users WHERE salary > 50000";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            return user;
        });
    }

    public List<User> selectFailAndSalary(){
        final String QUERY = "SELECT name FROM users WHERE salary > 70000 AND NOT pass;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setName(rs.getString("name"));
            return user;
        });
    }

    public void updatePass(){
        final String QUERY = "UPDATE users SET pass = 1 WHERE grade >= 50;";

        jdbcTemplate.update(QUERY);
    }

}
