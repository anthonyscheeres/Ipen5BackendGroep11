package nl.Ipsen5Server.Data;

import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;


public interface BatchDAO {

	
	  /**
    *
    * @author Anthony Scheeres
    *
    */
	@SqlQuery("INSERT INTO Platform(PlatformName) VALUES(:Platform); INSERT INTO ContactPersoon(CustomMessage) VALUES (:CustomMessage); INSERT INTO Contact(Username, Platform) VALUES (:User, :Platform);")
	void Insert(
			
			String email,
			 @Bind("Platform") String genoemde_social_media,
			 @Bind("CustomMessage") String message, 
			 String partial_IP, //not in db TODO: add to db
			String site, //not in db TODO: add to db
			String title, //not in db TODO: add to db
			String uid, //not in db TODO: add to db
			 @Bind("User") String user
			
			);
	
}
