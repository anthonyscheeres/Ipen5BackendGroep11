package nl.Ipsen5Server.Data;

import nl.Ipsen5Server.Domain.Colleague;
import nl.Ipsen5Server.Service.ColleagueMapper;
import org.jdbi.v3.sqlobject.config.RegisterRowMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.statement.SqlQuery;

import java.util.ArrayList;

@RegisterRowMapper(ColleagueMapper.class)
public interface ColleagueDAO {
    @SqlQuery("SELECT * FROM Medewerker")
    ArrayList<Colleague> getAll();

    @SqlQuery("SELECT * FROM Medewerker WHERE Email = :Email")
    Colleague getTemplateByEmail(
            @Bind("Email") String Email
    );
}

