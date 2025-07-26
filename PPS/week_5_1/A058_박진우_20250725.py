class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next    # 다음 노드를 기억해두고
            curr.next = prev         # 현재 노드의 next를 뒤로 연결
            prev = curr              # prev를 한 칸 앞으로
            curr = next_node         # curr도 다음으로 이동

        return prev  # prev는 새로운 head가 됨
