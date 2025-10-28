export default {
  async fetch(request, env) {
    const authKey = request.headers.get("X-Auth-Key");
    if (authKey !== env.AUTH_KEY) {
      return new Response("Unauthorized", { status: 403 });
    }

    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "*",
        },
      });
    }

    const backendUrl = env.BACKEND_URL;
    const newRequest = new Request(backendUrl, {
      method: request.method,
      headers: request.headers,
      body: request.body,
    });

    try {
      const resp = await fetch(newRequest);
      const headers = new Headers(resp.headers);
      headers.set("Access-Control-Allow-Origin", "*");
      headers.set("Access-Control-Expose-Headers", "Content-Disposition");

      const contentDisposition = resp.headers.get("Content-Disposition");
      if (contentDisposition) headers.set("Content-Disposition", contentDisposition);

      return new Response(resp.body, {
        status: resp.status,
        statusText: resp.statusText,
        headers,
      });
    } catch (err) {
      console.error("Error fetching backend:", err);
      return new Response("Error fetching backend", { status: 500 });
    }
  },
};
