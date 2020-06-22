
package nl.Ipsen5Server.Data;

import nl.Ipsen5Server.Domain.Message;
import nl.Ipsen5Server.Service.MessageMapper;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;

import java.util.ArrayList;

@RegisterRowMapper(MessageMapper.class)
public interface MessageDAO {

    @SqlQuery("SELECT * FROM MessageTemplate")
    ArrayList<Message> getAllTemplates();

    @SqlUpdate("DELETE FROM MessageTemplate WHERE MessageID = :MessageID")
    void deleteTemplateByMessageID(
            @Bind("MessageID") String MessageID
    );

    @SqlQuery("SELECT * FROM MessageTemplate WHERE MessageID = :MessageID")
    Message getTemplateByMessageID(
            @Bind("MessageID") String MessageID
    );


    @SqlUpdate("INSERT INTO MessageTemplate(MessageID, Message, Info)" +
            " VALUES (:MessageID,:Message,:Info)")
    void uploadNewMessage(
            @Bind("MessageID") String MessageID,
            @Bind("Message") String Message,
            @Bind("Info") String Info
    );

}
