package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.Colleague;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;

import java.sql.ResultSet;
import java.sql.SQLException;

public class ColleagueMapper implements RowMapper<Colleague> {

    public Colleague map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new Colleague(
                rs.getString("Email"),
                rs.getString("Userpassword"),
                rs.getString("Usertype")
        );
    }
}