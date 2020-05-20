package nl.Ipsen5Server.Presentation;

import nl.Ipsen5Server.Data.MessageDAO;
import nl.Ipsen5Server.Domain.Message;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.ArrayList;
import java.util.List;

@Path("/messagetemplate")
public class MessageResource {

    private MessageDAO dao;

    public MessageResource(MessageDAO dao) {
        this.dao = dao;
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getAllTemplates() {
        ArrayList<Message> allTemplates = dao.getAllTemplates();

        if (allTemplates == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(allTemplates, MediaType.APPLICATION_JSON).build();
    }


    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/id/{MessageID}")
    public Response findTemplateByMessageID(
            @PathParam("MessageID") String MessageID) {

        System.out.println("HET ID: " + MessageID);
        Message message = dao.getTemplateByMessageID(MessageID);

        if (message == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(message, MediaType.APPLICATION_JSON).build();
    }


    @POST
    @Path("/delete")
    public Response deleteTemplate(
        @FormParam("MessageID") String MessageID
    ){
        dao.deleteTemplateByMessageID(MessageID);

        return Response.ok()
                .entity("Deleted template with id: ' " + MessageID + " '  successfully")
                .build();
    }


}
