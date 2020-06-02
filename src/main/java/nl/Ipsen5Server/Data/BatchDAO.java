package nl.Ipsen5Server.Data;

import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.jdbi.v3.sqlobject.transaction.Transaction;


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


    );

    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(
        "INSERT INTO ContactPersoon(UserID, CustomMessage) VALUES (CONCAT(MD5(:User), MD5(:Platform)), :CustomMessage); "

    )

    void InsertContactPersoon(


        @Bind("Platform") String genoemde_social_media,
        @Bind("CustomMessage") String message,
        @Bind("User") String user

    );

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

    );

    /**
     *
     * @author Anthony Scheeres
     *
     */
    @Transaction
    @SqlUpdate(


        "UPDATE ContactPersoon SET Info = :Info WHERE UserID = CONCAT(MD5(:User), MD5(:Platform)); "

    )

    void UpdateInfo(


        @Bind("Info") String partial_IP

    );




}