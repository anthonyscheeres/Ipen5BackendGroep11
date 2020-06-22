package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.ContactPerson;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;

import java.sql.ResultSet;
import java.sql.SQLException;

public class ContactPersonMapper implements RowMapper<ContactPerson> {

    public ContactPerson map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new ContactPerson(
                rs.getString("userId"),
                rs.getString("ContactName"),
                rs.getString("OriginalPost"),
                rs.getString("CustomMessage"),
                rs.getString("SocialMedia"),
                rs.getString("Info")
        );
    }
}