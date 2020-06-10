package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.ContactPerson;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;

import java.sql.ResultSet;
import java.sql.SQLException;

public class ContactPersonMapper implements RowMapper<ContactPerson> {

    public ContactPerson map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new ContactPerson(
                rs.getString("name"),
                rs.getString("sendMessage"),
                rs.getString("description"),
                rs.getString("socialMedia"),
                rs.getString("userName")
        );
    }
}