package nl.Ipsen5Server.Data;

import nl.Ipsen5Server.Domain.User;
import nl.Ipsen5Server.Service.UserMapper;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;

import java.util.ArrayList;
import java.util.UUID;

@RegisterRowMapper(UserMapper.class)
public interface UserDAO {

    @SqlUpdate("DELETE FROM Medewerker WHERE Email = :Email")
    void deleteByEmail(
            @Bind("Email") String Email
    );

    @SqlQuery("SELECT * FROM Medewerker")
    ArrayList<User> getAll();

    @SqlQuery("SELECT * FROM Medewerker WHERE Email = :Email")
    User getUserByEmail(@Bind("Email") String Email);


}
