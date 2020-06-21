package nl.Ipsen5Server.Service;

import nl.Ipsen5Server.Domain.Batch;
import nl.Ipsen5Server.Domain.Message;
import org.jdbi.v3.core.mapper.RowMapper;
import org.jdbi.v3.core.statement.StatementContext;

import java.sql.ResultSet;
import java.sql.SQLException;

public class BatchMapper implements RowMapper<Batch> {

    @Override
    public Batch map(ResultSet rs, StatementContext ctx) throws SQLException {
        return new Batch(
                rs.getString("BatchID"),
                rs.getString("BatchName"),
                rs.getString("StandardMessage")
        );
    }
}
