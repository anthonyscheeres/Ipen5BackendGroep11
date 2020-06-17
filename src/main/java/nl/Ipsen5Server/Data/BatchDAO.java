package nl.Ipsen5Server.Data;

import java.sql.SQLException;

import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.jdbi.v3.sqlobject.transaction.Transaction;
import org.json.JSONObject;

import com.fasterxml.jackson.jaxrs.json.annotation.JSONP;

import nl.Ipsen5Server.Domain.Dump;


public interface BatchDAO {


    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(

        "INSERT INTO Platform(PlatformName) VALUES(:Platform); "

    )

    void InsertPlatform(

        @Bind("Platform") String genoemde_social_media

    	    ) throws  SQLException;

    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(
    		
        "INSERT INTO ContactPersoon(UserID, CustomMessage, ContactName) VALUES (CONCAT(MD5(:User), MD5(:Platform)), 'Leeg', :User); "

    )

    void InsertContactPersoon (


        @Bind("Platform") String genoemde_social_media,

        
        @Bind("User") String user

    ) throws  SQLException;

    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(


        "INSERT INTO Contact(Username, Platform, UserID) VALUES (:User, :Platform, CONCAT(MD5(:User), MD5(:Platform))); "

    )

    void InsertContact(

        @Bind("Platform") String genoemde_social_media,

        @Bind("User") String user

    	    ) throws  SQLException;

    

    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(


        "INSERT INTO BatchContactPersoon(ContactPersoon, Batch) VALUES (CONCAT(MD5(:User), MD5(:Platform)), :Batch);"

    )

    void InsertContactBatch(


            @Bind("User") String contactPersoon,
            
            @Bind("Platform") String platform,

            @Bind("Batch") String batch

    	    ) throws  SQLException;
    
    
    
    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(


        "UPDATE ContactPersoon SET Info = :Info, OriginalPost = :CustomMessage WHERE UserID = CONCAT(MD5(:User), MD5(:Platform)); "

    )

    void UpdateInfo(

    	@Bind("CustomMessage") String message,
        @Bind("Info") String partial_IP,
     
        
        @Bind("Platform") String platform,
        @Bind("User") String contactPersoon

    	    ) throws  SQLException;


    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(


        "INSERT INTO Batch(BatchID, BatchName) VALUES (:Batch, :Batch); "

    ) 

    void InsertBatch(


            @Bind("Batch") String batch

    	    ) throws  SQLException;

    @SqlQuery(

           "SELECT * FROM BatchContactPersoon"
           + " left join Batch on BatchContactPersoon.Batch = Batch.BatchID"
           + " left join ContactPersoon on BatchContactPersoon.ContactPersoon = ContactPersoon.UserID"
           + " left join Contact on Contact.Username = ContactPersoon.UserID"
           + " left join Platform on Contact.Platform = Platform.PlatformName; "
    		
        )
    JSONObject SelectBatches() ;
    
    

  
   @SqlQuery(

          "SELECT * FROM BatchContactPersoon"
          + " left join Batch on BatchContactPersoon.Batch = Batch.BatchID"
          + " left join ContactPersoon on BatchContactPersoon.ContactPersoon = ContactPersoon.UserID"
          + " left join Contact on Contact.Username = ContactPersoon.UserID"
          + " left join Platform on Contact.Platform = Platform.PlatformName WHERE Batch = :Batch; "
   		
       )
   JSONObject SelectSpecificBatches(
			
			 @Bind("Batch") String batch
			) ;

   @JSONP
   @SqlQuery("SELECT * FROM Batch;")
   JSONObject SelectBatchNames();


}