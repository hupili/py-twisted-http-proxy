# Why and How

   * I need to log HTTP traces for studies.
   * There are many proxies but only text interface (stdin/stdout, log, etc) is available.
   * It will be more convenient to intercept activities inside Python.
   * Twisted provides the "proxy" protocol and I really do nothing here.
   * Twisted doc is twisted and I believe it takes time for novice users to find a proper intercept point.
   * Then comes this snippet as a short note.
