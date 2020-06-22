
package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.User;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.UUID;

public class UserMapper implements RowMapper<User> {

    public User map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new User(
                rs.getString("Email"),
                rs.getString("UserPassword"),
                rs.getString("Usertype")
        );
    }

}