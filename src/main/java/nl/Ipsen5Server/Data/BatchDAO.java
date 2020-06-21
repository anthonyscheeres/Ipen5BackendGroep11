package nl.Ipsen5Server.Data;

import java.util.List;
import java.util.Map;

import org.jdbi.v3.core.statement.UnableToExecuteStatementException;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.jdbi.v3.sqlobject.transaction.Transaction;

import org.jdbi.v3.core.mapper.*; 



@RegisterRowMapper(MapMapper.class)
public interface BatchDAO {


    /**
     *
     * @author Anthony Scheeres
     *
     */

    @SqlUpdate(

        "INSERT INTO Platform(PlatformName) VALUES(:Platform); "

    )
    @Transaction
    void InsertPlatform(

        @Bind("Platform") String genoemde_social_media

    	    ) throws UnableToExecuteStatementException;

    /**
     *
     * @author Anthony Scheeres
     *
     */

    @SqlUpdate(
    		
        "INSERT INTO ContactPersoon(UserID, CustomMessage, ContactName) VALUES (CONCAT(MD5(:User), MD5(:Platform)), 'Leeg', :User); "

    )
    @Transaction
    void InsertContactPersoon (


        @Bind("Platform") String genoemde_social_media,

        
        @Bind("User") String user

    ) throws  UnableToExecuteStatementException;

    /**
     *
     * @author Anthony Scheeres
     *
     */

    @SqlUpdate(


        "INSERT INTO Contact(Username, Platform, UserID) VALUES (:User, :Platform, CONCAT(MD5(:User), MD5(:Platform))); "

    )
    @Transaction
    void InsertContact(

        @Bind("Platform") String genoemde_social_media,

        @Bind("User") String user

    	    ) throws UnableToExecuteStatementException;

    

    /**
     *
     * @author Anthony Scheeres
     *
     */

    @SqlUpdate(


        "INSERT INTO BatchContactPersoon(ContactPersoon, Batch) VALUES (CONCAT(MD5(:User), MD5(:Platform)), :Batch);"

    )
    @Transaction
    void InsertContactBatch(


            @Bind("User") String contactPersoon,
            
            @Bind("Platform") String platform,

            @Bind("Batch") String batch

    	    ) throws UnableToExecuteStatementException;
    
    
    
    /**
     *
     * @author Anthony Scheeres
     *
     */


    
    @SqlUpdate(

        "UPDATE ContactPersoon SET Info = :Info, OriginalPost = :CustomMessage WHERE UserID = CONCAT(MD5(:User), MD5(:Platform)); "

    )
    @Transaction
    void UpdateInfo(

    	@Bind("CustomMessage") String message,
        @Bind("Info") String partial_IP,
     
        
        @Bind("Platform") String platform,
        @Bind("User") String contactPersoon

    	    );


    
    
    
    
    
    
    /**
     *
     * @author Anthony Scheeres
     *
     */

    @SqlUpdate(

    	
        "INSERT INTO Batch(BatchID, BatchName) VALUES (:Batch, :Batch); "

    ) 
    @Transaction
    void InsertBatch(


            @Bind("Batch") String batch

    	    ) throws UnableToExecuteStatementException;

    @SqlQuery(
           "SELECT Platform, Username FROM BatchContactPersoon "
           + "right join Batch on BatchContactPersoon.Batch = Batch.BatchID "
           + "right join ContactPersoon on BatchContactPersoon.ContactPersoon = ContactPersoon.UserID "
           + "right join Contact on Contact.UserID = ContactPersoon.UserID "
           + "right join Platform on Contact.Platform = Platform.PlatformName; "
    		
        )
    List<Map<String, Object>> SelectBatches() ;
    
<<<<<<< refs/remotes/origin/master
=======
   

   @SqlQuery(

          "SELECT Platform, Username FROM BatchContactPersoon "
          + "right join Batch on BatchContactPersoon.Batch = Batch.BatchID "
          + "right join ContactPersoon on BatchContactPersoon.ContactPersoon = ContactPersoon.UserID "
          + "right join Contact on Contact.UserID = ContactPersoon.UserID right join Platform on Contact.Platform = Platform.PlatformName "
          + "WHERE Batch = :Batch; "
   		
       )
   List<Map<String, Object>> SelectSpecificBatches(
			
			 @Bind("Batch") String batch
			) ;
>>>>>>> resolved unable to do full join with batches bug

   @SqlQuery("SELECT * FROM Batch;")
   List<Map<String, Object>> SelectBatchNames();


}