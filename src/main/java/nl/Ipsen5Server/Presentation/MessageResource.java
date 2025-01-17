package nl.Ipsen5Server.Presentation;

import nl.Ipsen5Server.Data.MessageDAO;
import nl.Ipsen5Server.Domain.Message;
import nl.Ipsen5Server.Service.APIstarter;

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
    		
            @PathParam("MessageID") String MessageID
            
            ) {
    	
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

    @POST
    @Path("/new")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response createNewTemplate(
            @FormParam("MessageID") String MessageID,
            @FormParam("Message") String Message,
            @FormParam("Info") String Info
    ) {
        dao.uploadNewMessage(MessageID, Message, Info);

        return Response.ok()
                .entity("New template successfully created with id: " + MessageID + ". The message: " + Message)
                .build();
    }

    @POST
    @Path("/send")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response createNewTemplate(
            @FormParam("Message") String Message,
            @FormParam("Users") String Users
    ) {
        String[] userList = Users.replace("[", "").replace("]", "").split(",");
        ArrayList<String> userArrayList  = new ArrayList<String>();
        for (String i:userList){
            userArrayList.add(i);
        }

        APIstarter i = new APIstarter();
        i.SendMessageKik(Message, userArrayList);

        return Response.ok()
                .entity("Successfully sent: " + Message + "To: " + Users)
                .build();
    }


}
