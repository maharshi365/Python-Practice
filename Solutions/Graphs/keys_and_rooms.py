class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        keys = rooms[0]
        left_to_visit = list(range(1, len(rooms)))

        while(len(keys) > 0):
            curr_room = keys[0]
            if curr_room in left_to_visit:
                keys = keys + rooms[curr_room]
                keys.pop(0)
                left_to_visit.remove(curr_room)
            else:
                keys.pop(0)
        if (len(left_to_visit) == 0):
            return True
        else:
            return False
