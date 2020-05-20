package nl.Ipsen5Server.Domain;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Message {

    private String MessageID;
    private String Message;
    private String Info;

    @JsonCreator
    public Message(String MessageID, String Message, String Info) {
        this.MessageID = MessageID;
        this.Message = Message;
        this.Info = Info;
    }

    @JsonProperty
    public String getMessageID() {
        return MessageID;
    }

    @JsonProperty
    public String getMessage() {
        return Message;
    }

    @JsonProperty
    public String getInfo() {
        return Info;
    }


}
