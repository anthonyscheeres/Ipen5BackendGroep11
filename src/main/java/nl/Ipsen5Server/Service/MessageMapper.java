package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.Message;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;

import java.sql.ResultSet;
import java.sql.SQLException;

public class MessageMapper implements RowMapper<Message> {

    @Override
    public Message map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new Message(
                rs.getString("MessageID"),
                rs.getString("Message"),
                rs.getString("Info")
        );
    }
}