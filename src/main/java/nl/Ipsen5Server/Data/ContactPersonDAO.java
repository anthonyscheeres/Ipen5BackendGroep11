package nl.Ipsen5Server.Data;

import nl.Ipsen5Server.Domain.ContactPerson;
import nl.Ipsen5Server.Domain.Message;
import nl.Ipsen5Server.Service.ContactPersonMapper;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;

import java.util.ArrayList;

@RegisterRowMapper(ContactPersonMapper.class)
public interface ContactPersonDAO {
    @SqlQuery("SELECT * FROM ContactPerson")
    ArrayList<ContactPerson> getAll();

    @SqlQuery("SELECT * FROM ContactPerson WHERE UserId = :ContactPersonID")
    ContactPerson getTemplateByContactPersonID(
            @Bind("ContactPersonID") String ContactPersonID
    );
}

