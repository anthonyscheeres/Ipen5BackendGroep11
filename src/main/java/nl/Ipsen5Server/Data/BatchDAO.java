package nl.Ipsen5Server.Data;

import org.jdbi.v3.sqlobject.statement.SqlQuery;


public interface BatchDAO {

	
	
	@SqlQuery("")
	void Insert(String email, String genoemde_social_media, String message, String partial_IP, String site,
			String title, String uid, String user);
	
}
