package nl.Ipsen5Server.Domain;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Batch {

        private String BatchID;
        private String BatchName;
        private String StandardMessage;

        @JsonCreator
        public Batch(String BatchID, String BatchName, String StandardMessage) {
            this.BatchID = BatchID;
            this.BatchName = BatchName;
            this.StandardMessage = StandardMessage;
        }

        @JsonProperty
        public String getBatchID() {
            return BatchID;
        }

        @JsonProperty
        public String getBatchName() {
            return BatchName;
        }

        @JsonProperty
        public String getStandardMessage() {
            return StandardMessage;
        }


    }
