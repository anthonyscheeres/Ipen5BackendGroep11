package nl.Ipsen5Server.Data;

import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;


public interface BatchDAO {

	
	  /**
    *
    * @author Anthony Scheeres
    *
    */
	@SqlQuery(
			
			"INSERT INTO Platform(PlatformName) VALUES(:Platform); "
			+ "INSERT INTO ContactPersoon(UserID) VALUES (CONCAT(MD5(:User), MD5(:Platform))); "  //TODO: this query seems a little too long
			+ "INSERT INTO Contact(Username, Platform, UserID) VALUES (:User, :Platform, CONCAT(MD5(:User), MD5(:Platform))); "
			+ "UPDATE ContactPersoon SET CustomMessage = :CustomMessage, Info = :Info WHERE UserID = CONCAT(MD5(:User), MD5(:Platform)); "
			
			)
	
	void Insert(
			
			String email,
			 @Bind("Platform") String genoemde_social_media,
			 @Bind("CustomMessage") String message, 
			@Bind("Info") String partial_IP, //not right name in db TODO: add to db
			String site, //not in db TODO: add to db
			String title, //not in db TODO: add to db
			String uid, //not in db TODO: add to db
			 @Bind("User") String user
			
			);
	
}
