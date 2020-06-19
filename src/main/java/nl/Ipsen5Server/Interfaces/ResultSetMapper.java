package nl.Ipsen5Server.Interfaces;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Map;

import org.jdbi.v3.core.statement.StatementContext;

public interface ResultSetMapper<T> {
	 public Map<String, Object> map(int index, ResultSet r, StatementContext ctx) throws SQLException; 
}
