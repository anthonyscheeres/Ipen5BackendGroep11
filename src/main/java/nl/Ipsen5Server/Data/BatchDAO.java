package nl.Ipsen5Server.Data;

import java.sql.SQLException;

import org.jdbi.v3.core.statement.UnableToExecuteStatementException;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.jdbi.v3.sqlobject.transaction.Transaction;
import org.json.JSONObject;

import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.jaxrs.json.annotation.JSONP;

import nl.Ipsen5Server.Domain.Dump;


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


}