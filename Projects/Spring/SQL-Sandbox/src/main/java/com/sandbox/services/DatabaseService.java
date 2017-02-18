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
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
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
            user.setFields("Name;Email;Salary");
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
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
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
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
            return user;
        });
    }

    public List<User> selectFailAndSalary(){
        final String QUERY = "SELECT name FROM users WHERE salary > 70000 AND NOT pass;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setName(rs.getString("name"));
            user.setFields("name");
            return user;
        });
    }

    public void updatePass(){
        final String QUERY = "UPDATE users SET pass = 1 WHERE grade >= 50;";

        jdbcTemplate.update(QUERY);
    }

    public void deleteFailing(){
        final String QUERY = "DELETE FROM users WHERE NOT pass";
        jdbcTemplate.execute(QUERY);
    }

    public List<User> selectLike(){
        final String QUERY = "SELECT * FROM users WHERE salary LIKE ____%0;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
            return user;
        });
    }

    public List<User> selectTop(){
        final String QUERY = "SELECT * FROM users LIMIT 5;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
            return user;
        });
    }

    public List<User> selectOrder(){
        final String QUERY = "SELECT * FROM users ORDER BY salary, name;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setId(rs.getInt("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setSalary(rs.getInt("salary"));
            user.setGrade(rs.getInt("grade"));
            user.setPass(rs.getBoolean("pass"));
            user.setFields("Id;Name;Email;Salary;Grade;Pass");
            return user;
        });
    }

    public List<User> selectGroup(){
        final String QUERY = "SELECT name, SUM(salary) FROM users GROUP BY name;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setName(rs.getString("name"));
            user.setSum(rs.getInt(2));
            user.setFields("Name;Sum");
            return user;
        });
    }

    public List<User> selectDistinct(){
        final String QUERY = "SELECT DISTINCT salary FROM users;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setSalary(rs.getInt("salary"));
            user.setFields("Salary");
            return user;
        });
    }

    public List<User> selectSort() {
        final String QUERY = "SELECT name, email FROM users ORDER BY CASE " +
                "WHEN email REGEXP '.@uwaterloo.ca' THEN 1 " +
                "WHEN email REGEXP '.@hotmail.com' THEN 2 " +
                "WHEN email REGEXP '.@gmail.com' THEN 3 " +
                "ELSE 4 END ASC;";
        return jdbcTemplate.query(QUERY, (rs, id) -> {
            User user = new User();
            user.setEmail(rs.getString("email"));
            user.setName(rs.getString("name"));
            user.setFields("Name;Email");
            return user;
        });
    }
}
