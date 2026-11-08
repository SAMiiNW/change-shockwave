# Operations Screen service document

Operations Screen reads service summaries from Queue Worker and gateway health counters. Its own interface is not directly changed. It becomes stale when either upstream path stops producing data.

