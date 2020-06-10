package nl.Ipsen5Server.Presentation;

import nl.Ipsen5Server.Data.ContactPersonDAO;
import nl.Ipsen5Server.Domain.ContactPerson;
import nl.Ipsen5Server.Domain.Message;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.ArrayList;
import java.util.List;

@Path("/contactPerson")
public class ContactPersonResource {

    private ContactPersonDAO dao;

    public ContactPersonResource(ContactPersonDAO dao) {
		super();
		this.dao = dao;
	}

	@GET
    public List<ContactPerson> getAll() { return dao.getAll(); }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/id/{ContactPersonID}")
    public Response findTemplateByMessageID(
            @PathParam("ContactPersonID") String ContactPersonID) {

        System.out.println("HET ID: " + ContactPersonID);
        ContactPerson contactPerson = dao.getTemplateByContactPersonID(ContactPersonID);

        if (contactPerson == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(contactPerson, MediaType.APPLICATION_JSON).build();
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/all")
    public Response getAllContactPersons() {
        ArrayList<ContactPerson> allContactPersons = dao.getAll();

        if (allContactPersons == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(allContactPersons, MediaType.APPLICATION_JSON).build();
    }
}
