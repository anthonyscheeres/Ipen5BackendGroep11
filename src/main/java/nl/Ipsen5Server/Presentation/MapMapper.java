package nl.Ipsen5Server.Presentation;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

import org.jdbi.v3.core.statement.StatementContext;

import nl.Ipsen5Server.Interfaces.ResultSetMapper;

public class MapMapper implements ResultSetMapper<Map<String, Object>> {
    @Override
    public Map<String, Object> map(int index, ResultSet r, StatementContext ctx) throws SQLException {
        Map<String, Object> map = new HashMap<String, Object>();
        for (int i = 1; i <= r.getMetaData().getColumnCount(); i++) {
            map.put(r.getMetaData().getColumnLabel(i), r.getObject(i));
        }
        return map;
    }
}