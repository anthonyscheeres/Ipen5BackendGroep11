package nl.Ipsen5Server.Data;

import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;


public interface BatchDAO {

	
	
	@SqlQuery("INSERT INTO Platform(PlatformName) VALUES(:Platform); INSERT INTO Contact(Username, Platform) VALUES (:User, :Platform);")
	void Insert(
			
			String email,
			 @Bind("Platform") String genoemde_social_media,
			 @Bind("Message") String message, 
			 String partial_IP, 
			String site,
			String title, 
			String uid, 
			 @Bind("User") String user
			
			);
	
}
