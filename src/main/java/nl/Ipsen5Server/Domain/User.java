package nl.Ipsen5Server.Domain;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.glassfish.jersey.server.JSONP;
import javax.validation.constraints.NotNull;
import java.security.Principal;
import java.util.UUID;

public class User  {

    private String Email;
    private String UserPassword;
    private String Usertype;

    @JsonCreator
    public User(String Email, String UserPassword, String Usertype) {
        this.Email = Email;
        this.UserPassword = UserPassword;
        this.Usertype = Usertype;
    }

    @JsonProperty
    public String getEmail() {
        return Email;
    }

    @JsonProperty
    public String getUserPassword() {
        return UserPassword;
    }

    @JsonProperty
    public String getUsertype() {
        return Usertype;
    }


}
