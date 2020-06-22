package nl.Ipsen5Server.Domain;

public class ContactPerson {
    private String UserId;
    private String ContactName;
    private String OriginalPost;
    private String CustomMessage;
    private String SocialMedia;
    private String Info;

    public ContactPerson(String userId, String contactName, String originalPost, String customMessage, String socialMedia, String info) {
        super();
        this.UserId = userId;
        this.ContactName = contactName;
        this.OriginalPost = originalPost;
        this.CustomMessage = customMessage;
        this.SocialMedia = socialMedia;
        this.Info = info;
    }

    public String getUserId() {
        return UserId;
    }

    public void setUserId(String userId) {
        UserId = userId;
    }

    public String getContactName() {
        return ContactName;
    }

    public void setContactName(String contactName) {
        ContactName = contactName;
    }

    public String getOriginalPost() {
        return OriginalPost;
    }

    public void setOriginalPost(String originalPost) {
        OriginalPost = originalPost;
    }

    public String getCustomMessage() {
        return CustomMessage;
    }

    public void setCustomMessage(String customMessage) {
        CustomMessage = customMessage;
    }

    public String getSocialMedia() {
        return SocialMedia;
    }

    public void setSocialMedia(String socialMedia) {
        SocialMedia = socialMedia;
    }

    public String getInfo() {
        return Info;
    }

    public void setInfo(String info) {
        Info = info;
    }
}

