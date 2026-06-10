import urllib


class Assistant(object):
    def __init__(self, session):
        super(Assistant, self).__init__()
        self._session = session

    def getOrganizationAssistantCapabilities(self, organizationId: str):
        """
        **List the AI assistant's available capabilities and agents for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-capabilities

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["assistant", "configure", "capabilities"],
            "operation": "getOrganizationAssistantCapabilities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assistant/capabilities"

        return self._session.get(metadata, resource)

    def createOrganizationAssistantChatCompletion(self, organizationId: str, **kwargs):
        """
        **Create a chat completion with the AI assistant**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-assistant-chat-completion

        - organizationId (string): Organization ID
        - query (string): Simple text question or instruction to send to the AI assistant. Provide either 'query' for text-only requests or 'content' for multi-modal input.
        - content (array): List of multi-modal content blocks. Use instead of 'query' to send text or images. Supports text and image types only; for audio and file support, use the messages endpoint. Maximum 8 parts.
        - threadId (string): An existing thread ID to continue a conversation. If omitted, a new thread is created.
        - networkId (string): Optional network ID to scope the query to a specific network. Defaults to the user's last visited network.
        - platform (string): Platform identifier. Defaults to MERAKI when omitted. Case-insensitive.
        - language (string): Optional language override. Defaults to the user's preferred language.
        - country (string): Optional country override. Defaults to the user's country.
        """

        kwargs.update(locals())

        if "platform" in kwargs:
            options = ["DIGITAL_TWIN", "DNAC", "MERAKI", "digital_twin", "dnac", "meraki"]
            assert kwargs["platform"] in options, (
                f'''"platform" cannot be "{kwargs["platform"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["assistant", "configure", "chat", "completions"],
            "operation": "createOrganizationAssistantChatCompletion",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/completions"

        body_params = [
            "query",
            "content",
            "threadId",
            "networkId",
            "platform",
            "language",
            "country",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAssistantChatCompletion: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssistantChatThreads(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List all active conversation threads for the authenticated user.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-threads

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): Number of entries per page. Defaults to 100. Maximum 1000.
        - sort (string): Field to sort results by. Defaults to dateModified.
        - sortOrder (string): Sort direction for results. Defaults to desc.
        - from (string): Filter threads modified after this timestamp.
        - to (string): Filter threads modified before this timestamp.
        """

        kwargs.update(locals())

        if "sort" in kwargs:
            options = ["dateModified", "id", "name"]
            assert kwargs["sort"] in options, f'''"sort" cannot be "{kwargs["sort"]}", & must be set to one of: {options}'''
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads"],
            "operation": "getOrganizationAssistantChatThreads",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads"

        query_params = [
            "perPage",
            "sort",
            "sortOrder",
            "from",
            "to",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationAssistantChatThreads: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationAssistantChatThread(self, organizationId: str, **kwargs):
        """
        **Create a new conversation thread.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-assistant-chat-thread

        - organizationId (string): Organization ID
        - threadName (string): Display name for the new thread.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads"],
            "operation": "createOrganizationAssistantChatThread",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads"

        body_params = [
            "threadName",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAssistantChatThread: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssistantChatThread(self, organizationId: str, threadId: str):
        """
        **Return a single conversation thread.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads"],
            "operation": "getOrganizationAssistantChatThread",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}"

        return self._session.get(metadata, resource)

    def updateOrganizationAssistantChatThread(self, organizationId: str, threadId: str, threadName: str, **kwargs):
        """
        **Update the name of a conversation thread.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-assistant-chat-thread

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - threadName (string): New display name for the thread.
        """

        kwargs = locals()

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads"],
            "operation": "updateOrganizationAssistantChatThread",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}"

        body_params = [
            "threadName",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationAssistantChatThread: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAssistantChatThread(self, organizationId: str, threadId: str):
        """
        **Delete a conversation thread and all its messages.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-assistant-chat-thread

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads"],
            "operation": "deleteOrganizationAssistantChatThread",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}"

        return self._session.delete(metadata, resource)

    def getOrganizationAssistantChatThreadMessages(
        self, organizationId: str, threadId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List messages in a conversation thread.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread-messages

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): Number of entries per page. Defaults to 100. Maximum 1000.
        - sortOrder (string): Sort direction for results by timestamp. Defaults to asc.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages"],
            "operation": "getOrganizationAssistantChatThreadMessages",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages"

        query_params = [
            "perPage",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssistantChatThreadMessages: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationAssistantChatThreadMessage(self, organizationId: str, threadId: str, content: list, **kwargs):
        """
        **Create a new chat message in a thread.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-assistant-chat-thread-message

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - content (array): List of message content parts. Supports text, image, audio, and file types. Maximum 8 parts.
        - networkName (string): Name of the target network.
        - networkId (string): Optional Meraki network ID for thread context.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages"],
            "operation": "createOrganizationAssistantChatThreadMessage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages"

        body_params = [
            "content",
            "networkName",
            "networkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAssistantChatThreadMessage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssistantChatThreadMessage(self, organizationId: str, threadId: str, messageId: str):
        """
        **Return a single message in a conversation thread.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread-message

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - messageId (string): Message ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages"],
            "operation": "getOrganizationAssistantChatThreadMessage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        messageId = urllib.parse.quote(str(messageId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages/{messageId}"

        return self._session.get(metadata, resource)

    def getOrganizationAssistantChatThreadMessageArtifacts(self, organizationId: str, threadId: str, messageId: str):
        """
        **List artifacts attached to a specific message**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread-message-artifacts

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - messageId (string): Message ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages", "artifacts"],
            "operation": "getOrganizationAssistantChatThreadMessageArtifacts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        messageId = urllib.parse.quote(str(messageId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages/{messageId}/artifacts"

        return self._session.get(metadata, resource)

    def getOrganizationAssistantChatThreadMessageArtifact(
        self, organizationId: str, threadId: str, messageId: str, artifactId: str
    ):
        """
        **Return a single artifact with its full content.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread-message-artifact

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - messageId (string): Message ID
        - artifactId (string): Artifact ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages", "artifacts"],
            "operation": "getOrganizationAssistantChatThreadMessageArtifact",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        messageId = urllib.parse.quote(str(messageId), safe="")
        artifactId = urllib.parse.quote(str(artifactId), safe="")
        resource = (
            f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages/{messageId}/artifacts/{artifactId}"
        )

        return self._session.get(metadata, resource)

    def getOrganizationAssistantChatThreadMessageFeedback(self, organizationId: str, threadId: str, messageId: str):
        """
        **Return all feedback entries previously submitted for a specific message in a thread.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-chat-thread-message-feedback

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - messageId (string): Message ID
        """

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages", "feedback"],
            "operation": "getOrganizationAssistantChatThreadMessageFeedback",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        messageId = urllib.parse.quote(str(messageId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages/{messageId}/feedback"

        return self._session.get(metadata, resource)

    def createOrganizationAssistantChatThreadMessageFeedback(
        self, organizationId: str, threadId: str, messageId: str, vote: bool, **kwargs
    ):
        """
        **Submit or replace feedback for a specific assistant message.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-assistant-chat-thread-message-feedback

        - organizationId (string): Organization ID
        - threadId (string): Thread ID
        - messageId (string): Message ID
        - vote (boolean): True for positive, false for negative.
        - reason (string): Optional free-text reason for the feedback (e.g., 'inaccurate', 'incomplete', 'helpful'). Not constrained to a fixed set of values.
        - comment (string): Optional free-text comment providing additional detail.
        - message (string): The assistant message text the feedback refers to. Captured for analytics; not required.
        - prompt (string): The user prompt that produced the assistant message. Captured for analytics; not required.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["assistant", "configure", "chat", "threads", "messages", "feedback"],
            "operation": "createOrganizationAssistantChatThreadMessageFeedback",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        threadId = urllib.parse.quote(str(threadId), safe="")
        messageId = urllib.parse.quote(str(messageId), safe="")
        resource = f"/organizations/{organizationId}/assistant/chat/threads/{threadId}/messages/{messageId}/feedback"

        body_params = [
            "vote",
            "reason",
            "comment",
            "message",
            "prompt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAssistantChatThreadMessageFeedback: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssistantQueryLimits(self, organizationId: str):
        """
        **Get query limits for the AI assistant for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assistant-query-limits

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["assistant", "configure", "queryLimits"],
            "operation": "getOrganizationAssistantQueryLimits",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assistant/queryLimits"

        return self._session.get(metadata, resource)
