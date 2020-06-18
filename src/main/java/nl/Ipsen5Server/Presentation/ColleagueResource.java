package nl.Ipsen5Server.Presentation;

import nl.Ipsen5Server.Data.ColleagueDAO;
import nl.Ipsen5Server.Domain.Colleague;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.ArrayList;
import java.util.List;

@Path("/colleague")
public class ColleagueResource {

    private ColleagueDAO dao;

    public ColleagueResource(ColleagueDAO dao) {
		super();
		this.dao = dao;
	}

	@GET
    public List<Colleague> getAll() { return dao.getAll(); }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/all")
    public Response getAllColleagues() {
        ArrayList<Colleague> allColleagues = dao.getAll();

        if (allColleagues == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(allColleagues, MediaType.APPLICATION_JSON).build();
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/email/{Email}")
    public Response findTemplateByMessageID(
            @PathParam("Email") String Email) {

        System.out.println("De mail: " + Email);
        Colleague colleague = dao.getTemplateByEmail(Email);

        if (colleague == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(colleague, MediaType.APPLICATION_JSON).build();
    }
}
